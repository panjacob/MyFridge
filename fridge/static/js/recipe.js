function showRecipe(recipe){
    var wrapper = document.getElementById("wrapper"),
    h2 = document.createElement('h2'),
    description = document.createElement('p'),
    img = document.createElement('img');

    h2.setAttribute('class','item1')
    img.setAttribute('class','item3')
    description.setAttribute('class','item4')

    h2.innerHTML = recipe.name;
    img.setAttribute('src', '/static/recipes_img/' + recipe.img_name);
    img.setAttribute('height', '500');
    img.setAttribute('width', '500');
    description.innerHTML = recipe.long_description;

    var like = document.createElement('button');
    like.innerHTML = "Ulubione";

    wrapper.appendChild(img);
    wrapper.appendChild(h2);

    var div = document.createElement('div');
    div.setAttribute('id','ingridients');
    div.setAttribute('class','item2');

    wrapper.appendChild(div);

    var h2 = document.createElement('h2');
    h2.innerHTML = "Składniki";

    var target = document.getElementById("ingridients");
        target.appendChild(h2);

    recipe.products.forEach(function (item) {
        var product = document.createElement('p');
        product.innerHTML = item;

        target.appendChild(product);

    });

    wrapper.appendChild(description);
}

function close_window() {
    if (confirm("Close Window?")) {
        close();
    }
}
