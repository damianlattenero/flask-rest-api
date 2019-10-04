from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from Model import db, CategorySchema, Category
import json
categories_schema = CategorySchema()
category_schema = CategorySchema()


class CategoryResource(Resource):
    @staticmethod
    def get():
        categories = Category.query.all()
        categories = categories_schema.dump(categories).data
        return {'status': 'success', 'data': categories}, 200

    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate data and deserialize inputs
        data = categories_schema.load(json_data)

        category = Category.query.filter_by(name=data['name']).first()
        if category:
            return {'message': 'Category already exists'}, 400
        category = Category(
            name=json_data['name']
        )

        db.session.add(category)
        db.session.commit()

        result = category_schema.dump(category)

        return {'status': 'success', 'data': result}, 201

    @staticmethod
    def put():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = categories_schema.load(json_data)
        if errors:
            return errors, 422
        category = Category.query.filter_by(id=data['id']).first()
        if not category:
            return {'message': 'Category does not exists'}, 400
        category.name = data['name']
        db.session.commit()

        result = category_schema.dump(category).data

        return {'status': 'success', 'data': result}, 204

    @staticmethod
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = categories_schema.load(json_data)
        if errors:
            return errors, 422
        category = Category.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = category_schema.dump(category).data

        return {'status': 'success', 'data': result}, 204
