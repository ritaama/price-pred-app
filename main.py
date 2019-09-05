from flask import Flask, render_template,redirect,flash,url_for

from form import prediction
from joblib import load
app = Flask(__name__)

app.config['SECRET_KEY'] = '333c2cf354eed88eb04f3aaacd00235e'
@app.route('/', methods=['GET','POST'])
def home():
    form = prediction()
    result = ''
    if form.validate_on_submit():
        data = [form.bedrooms.data,form.bathrooms.data,form.sqft_living.data,form.sqft_lot.data,form.floors.data,
                form.sqft_above.data,form.sqft_lot15.data,form.yr_built.data,form.condition.data,form.zipcode.data]

        model = load('model.joblib')
        result = model.predict([data])
        result = str(result).strip('[]')
        flash('The price is $' + result)
        return redirect(url_for('home'))
    return render_template('home.html', myform=form)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ =='__main__':
    app.run(debug=True,