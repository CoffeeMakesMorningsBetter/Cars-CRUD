from flask import Flask, redirect, render_template, url_for, request
from flask_modus import Modus
from car import Car

app = Flask(__name__)
modus = Modus(app)

cars = [Car("Toyota", "Corolla S", 2005), Car("Toyota", "Corolla S", 2004)]


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/cars')
def index():
    return render_template('index.html', cars=cars)


@app.route('/cars/new')
def new():
    return render_template('new.html')


@app.route('/cars', methods=['POST'])
def create():
    # get some data from the form via a post request
    cars.append(
        Car(
            request.form.get("make"), request.form.get("model"),
            request.form.get("year")))
    return redirect(url_for('index'))


@app.route('/cars/<int:id>', methods=["GET", "PATCH"])
def show(id):
    found_car = [car for car in cars if car.id == id][0]
    if request.method == b"PATCH":
        found_car.make = request.form.get("make")
        found_car.model = request.form.get("model")
        found_car.year = request.form.get("year")
        return redirect(url_for('index'))
    return render_template('show.html', car=found_car)


@app.route('/cars/<int:id>/edit')
def edit(id):
    found_car = [car for car in cars if car.id == id][0]
    return render_template('edit.html', car=found_car)


@app.route('/cars/<int:id>', methods=['DELETE'])
def destroy(id):
    found_car = [car for car in cars if car.id == id][0]
    cars.remove(found_car)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=3000)
