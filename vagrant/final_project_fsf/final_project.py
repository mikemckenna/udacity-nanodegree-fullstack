from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///finalproject_fsf.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

# Application Routes


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    breadcrumbs = [{'text': 'Home', 'href': '/'},
                   {'text': 'Restaurants'}]
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', breadcrumbs=breadcrumbs, restaurants=restaurants)


@app.route('/restaurant/new', methods=['GET', 'POST'])
def newRestaurant():
    breadcrumbs = [{'text': 'Home', 'href': '/'},
                   {'text': 'Restaurants', 'href': '/restaurants'},
                   {'text': 'New'}]
    if request.method == 'POST':
        # print request.form
        # print request.args
        # print request.values
        newRestaurant = Restaurant(name=request.form['name'])
        session.add(newRestaurant)
        session.commit()
        flash("New restaurant has been added!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('restaurant_new.html', breadcrumbs=breadcrumbs)


@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    breadcrumbs = [{'text': 'Home', 'href': '/'},
                   {'text': 'Restaurants', 'href': '/restaurants'},
                   {'text': 'Edit'}]
    editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()

    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
            session.add(editedRestaurant)
            session.commit()
            flash("Restaurant has been updated!")
            return redirect(url_for('showRestaurants'))
    else:
        return render_template('restaurant_edit.html', breadcrumbs=breadcrumbs, restaurant=editedRestaurant)


@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    breadcrumbs = [{'text': 'Home', 'href': '/'},
                   {'text': 'Restaurants', 'href': '/restaurants'},
                   {'text': 'Delete'}]
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()

    if request.method == 'POST':
        session.delete(restaurant)
        session.commit()
        flash("Restaurant has been deleted from the database!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('restaurant_delete.html', breadcrumbs=breadcrumbs, restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    breadcrumbs = [{'text': 'Home', 'href': '/'},
                   {'text': 'Restaurants', 'href': '/restaurants'},
                   {'text': 'Menu'}]
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template('menu.html', breadcrumbs=breadcrumbs, restaurant=restaurant, items=items)


@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    breadcrumbs = [{'text': 'Home', 'href': '/'},
                   {'text': 'Restaurants', 'href': '/restaurants'},
                   {'text': 'Menu', 'href': '/restaurant/%s/menu' % restaurant_id},
                   {'text': 'New Item'}]
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()

    if request.method == 'POST':
        newMenuItem = MenuItem(name=request.form['name'],
                               course=request.form['course'],
                               description=request.form['description'],
                               price=request.form['price'],
                               restaurant_id=restaurant_id)
        session.add(newMenuItem)
        session.commit()
        flash("New menu item has been added!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('menu_item_new.html', breadcrumbs=breadcrumbs, restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    breadcrumbs = [{'text': 'Home', 'href': '/'},
                   {'text': 'Restaurants', 'href': '/restaurants'},
                   {'text': 'Menu', 'href': '/restaurant/%s/menu' % restaurant_id},
                   {'text': 'Edit Item'}]
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    editedMenuItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        editedMenuItem.name = request.form['name']
        editedMenuItem.course = request.form['course']
        editedMenuItem.description = request.form['description']
        editedMenuItem.price = request.form['price']
        editedMenuItem.restaurant_id = restaurant_id
        session.add(editedMenuItem)
        session.commit()
        flash("Menu item has been updated!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('menu_item_edit.html', breadcrumbs=breadcrumbs, restaurant=restaurant, item=editedMenuItem)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    breadcrumbs = [{'text': 'Home', 'href': '/'},
                   {'text': 'Restaurants', 'href': '/restaurants'},
                   {'text': 'Menu', 'href': '/restaurant/%s/menu' % restaurant_id},
                   {'text': 'Delete Item'}]
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    return render_template('menu_item_delete.html', breadcrumbs=breadcrumbs, restaurant=restaurant, item=item)


# JSON API Endpoints


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
