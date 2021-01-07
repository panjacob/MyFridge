let url_f = 'http://127.0.0.1:8000/fridge';

fetch(url_f)
    .then(res => res.json())
    .then((fridge_json) => {
        console.log('Checkout this JSON! ', fridge_json);

        showProducts(fridge_json)

    })
    .catch(err => {
        throw err
    });


function filterTable() {
    let dropdown, table, items, cells, product, filter;
    dropdown = document.getElementById("productDropdown");
    table = document.getElementById("Fridgeskey");
    items = table.getElementsByTagName("td");
    filter = dropdown.value;
    for (let item of items) {
        cells = item.getElementsByTagName("p");
        product = cells[1] || null;
        console.log(product)

        if (filter === "All" || !product || (filter === product.textContent)) {
            item.style.display = "";
        } else {
            item.style.display = "none";
        }
    }
}


function productsSearchByName() {
    var input, filter, table, td, tds, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("Fridgekey");
    td = table.getElementsByTagName("td");
    for (i = 0; i < td.length; i++) {
        tds = td[i].getElementsByTagName("p")[0];
        if (tds) {
            txtValue = tds.textContent || tds.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                td[i].style.display = "";
            } else {
                td[i].style.display = "none";
            }
        }
    }
}

function recipySearch() {

    var table, td, tds_id, tds_name, i, txtValue_id, txtValue_name;
    table = document.getElementById("Recipykey");
    td = table.getElementsByTagName("td");
    var result_id = [];
    var result_name = [];
    for (i = 0; i < td.length; i++) {
        tds_id = td[i].getElementsByTagName("p")[2];
        tds_name = td[i].getElementsByTagName("p")[0];
        if (tds_id) {
            txtValue_id = tds_id.textContent || tds_id.innerText;
            result_id[i] = txtValue_id;
        }
        if (tds_name) {
            txtValue_name = tds_name.textContent || tds_name.innerText;
            result_name[i] = txtValue_name;
        }

    }
    console.log(result_id);
    console.log(result_name);

}

function reply_click(clicked_id) {
    console.log(clicked_id);
}

var img = "https://blog.rahulbhutani.com/wp-content/uploads/2020/05/Screenshot-2018-12-16-at-21.06.29.png"
var recipies_data = {
    Recipies: [{
        id: 1,
        name: "Zupa",
        image_r: img,
        products: ["vanilla", "chocolate", "pistachio", "hard candy"],
        short_des: "Krotki opis.",
        description: "Tutaj bedzie opis."
    },
        {
            id: 2,
            name: "Chleb",
            image_r: img,
            products: ["vanilla", "chocolate", "pistachio", "hard candy"],
            short_des: "Krotki opis.",
            description: "Tutaj bedzie opis."
        },
        {
            id: 1,
            name: "Kanapka",
            image_r: img,
            products: ["vanilla", "chocolate", "pistachio", "hard candy"],
            short_des: "Krotki opis.",
            description: "Tutaj bedzie opis."
        },
        {
            id: 2,
            name: "Zapiekanka",
            image_r: img,
            products: ["vanilla", "chocolate", "pistachio", "hard candy"],
            short_des: "Krotki opis.",
            description: "Tutaj bedzie opis."
        },
        {
            id: 1,
            name: "Zupa",
            image_r: img,
            products: ["vanilla", "chocolate", "pistachio", "hard candy"],
            short_des: "Krotki opis.",
            description: "Tutaj bedzie opis."
        },
        {
            id: 2,
            name: "Chleb",
            image_r: img,
            products: ["vanilla", "chocolate", "pistachio", "hard candy"],
            short_des: "Krotki opis.",
            description: "Tutaj bedzie opis."
        },
        {
            id: 1,
            name: "Kanapka",
            image_r: img,
            products: ["vanilla", "chocolate", "pistachio", "hard candy"],
            short_des: "Krotki opis.",
            description: "Tutaj bedzie opis."
        },
        {
            id: 2,
            name: "Zapiekanka",
            image_r: img,
            products: ["vanilla", "chocolate", "pistachio", "hard candy"],
            short_des: "Krotki opis.",
            description: "Tutaj bedzie opis."
        },
        {
            id: 1,
            name: "Kanapka",
            image_r: img,
            products: ["vanilla", "chocolate", "pistachio", "hard candy"],
            short_des: "Krotki opis.",
            description: "Tutaj bedzie opis."
        },
        {
            id: 2,
            name: "Zapiekanka",
            image_r: img,
            products: ["vanilla", "chocolate", "pistachio", "hard candy"],
            short_des: "Krotki opis.",
            description: "Tutaj bedzie opis."
        }]
};

function recipyShow() {
    var wrapper_r = document.getElementById("recipies_wrapper");
    wrapper_r.innerHTML = "";

    recipies_data.Recipies.forEach(function (item) {
        var article = document.createElement('article'),
            h2 = document.createElement('h2'),
            p = document.createElement('p'),
            id = document.createElement('p'),
            img = document.createElement('img');


        article.setAttribute('class', 'col-sm');
        h2.innerHTML = item.name;
        img.setAttribute('src', item.image_r);
        img.setAttribute('height', '300');
        img.setAttribute('width', '300');
        p.innerHTML = item.short_des;
        id.innerHTML = item.id;
        id.hidden = true;

        var button = document.createElement('a');
        button.innerHTML = "Szczegoly";
        button.setAttribute('href', 'recipy.html');
        button.setAttribute('class', 'btn btn-primary');
        button.setAttribute('id', item.id);
        button.setAttribute('onClick', 'reply_click(this.id)');
        button.setAttribute('target', '_blank')


        var like = document.createElement('button');
        like.innerHTML = "Ulubione";

        article.appendChild(h2);
        article.appendChild(img);
        article.appendChild(p);
        article.appendChild(id);
        article.appendChild(button);

        wrapper_r.appendChild(article);
    });
}

function showProducts(fride_data) {
    var data = {
        Fridge: fride_data,
        Recipy: []
    };

    var byName = data.Fridge.slice(0);
    byName.sort(function (a, b) {
        var x = a.name.toLowerCase();
        var y = b.name.toLowerCase();
        return x < y ? -1 : x > y ? 1 : 0;
    });

    data.Fridge = byName;

    var tables = {};

    var moveMe = function () {
        this.table = tables[this.table === tables.Recipy ? 'Fridge' : 'Recipy'];
        this.table.tbody.appendChild(this.td);
    };

    Object.keys(data).forEach(function (key) {
        var container = document.createElement('div'),
            table = tables[key] = document.createElement('table'),
            tbody = table.tbody = document.createElement('tbody');
        if (key == 'Fridge') {
            container.setAttribute('id', 'fridge');
            var input = document.createElement("input");
            input.setAttribute('type', 'text')
            input.setAttribute('id', 'myInput')
            input.setAttribute('onkeyup', 'productsSearchByName()')
            input.setAttribute('placeholder', 'Search by names..')
            input.setAttribute('title', 'Type in a product name')
            container.append(input);
            var select = document.createElement("select");
            select.setAttribute("id", "productDropdown");
            select.setAttribute('oninput', "filterTable()")
            container.append(select);

            var opt0 = document.createElement("option");
            opt0.setAttribute("value", "All");
            var nod0 = document.createTextNode("All");
            opt0.appendChild(nod0);
            select.appendChild(opt0);
            var opt = document.createElement("option");
            opt.setAttribute("value", "fruit");
            var nod = document.createTextNode("fruit");
            opt.appendChild(nod);
            select.appendChild(opt);
            var opt2 = document.createElement("option");
            opt2.setAttribute("value", "spice");
            var nod2 = document.createTextNode("spice");
            opt2.appendChild(nod2);
            select.appendChild(opt2);
            var opt3 = document.createElement("option");
            opt3.setAttribute("value", "vegetable");
            var nod3 = document.createTextNode("vegetable");
            opt3.appendChild(nod3);
            select.appendChild(opt3);

        } else {
            container.setAttribute('id', 'recipy')

        }
        data[key].forEach(function (item) {
            var //tr = document.createElement('tr'),
                td = document.createElement('td');
            td.innerHTML = '<img src=' + 'static/products_img/' + item.img_name + ' width="140" height="140"/><p>' + item.name + '</p><br><p>' + item.type + '</p><p hidden>' + item.id + '<p>';
            //tr.appendChild(td);
            tbody.appendChild(td);
            var button = document.createElement('button');
            button.innerHTML = 'Move';
            button.onclick = moveMe;
            button.table = table;
            button.td = td;
            td.appendChild(button);
        });
        table.appendChild(tbody);
        var header = document.createElement('h2');
        header.innerHTML = key;
        container.appendChild(header);
        table.setAttribute('id', key + "key");
        container.appendChild(table);
        container.className = 'container';
        document.getElementById('wrapper').appendChild(container);

    });
    var search = document.getElementById('wrapper');
    var searchButton = document.createElement("button");
    //searchButton.setAttribute('onClick','recipySearch()');
    searchButton.setAttribute('onClick', 'recipyShow()');
    searchButton.setAttribute('id', "recipySearch")
    searchButton.innerHTML = 'Search';
    search.appendChild(searchButton);
};