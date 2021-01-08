let url_p = 'http://127.0.0.1:8000/products';
let url_f = 'http://127.0.0.1:8000/fridge';


fetch(url_p)
    .then(res => res.json())
    .then((products_json) => {
        console.log('Checkout this JSON! ', products_json);

        fetch(url_f)
            .then(res => res.json())
            .then((fridge_json) => {
                console.log('Checkout this JSON! ', fridge_json);

                showProducts(products_json, fridge_json)
            })
            .catch(err => {
                throw err
            });

    })
    .catch(err => {
        throw err
    });


function filterTable() {
    let dropdown, table, items, cells, product, filter;
    dropdown = document.getElementById("productDropdown");
    table = document.getElementById("Productskey");
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
    table = document.getElementById("Productskey");
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

    var table, td, tds, i, txtValue;
    table = document.getElementById("Fridgekey");
    td = table.getElementsByTagName("td");
    var result = [];
    for (i = 0; i < td.length; i++) {
        tds = td[i].getElementsByTagName("p")[2];

        if (tds) {
            txtValue = tds.textContent || tds.innerText;
            result[i] = txtValue;
        }

    }

    let cookie = document.getElementById("cid").innerHTML;

    fetch('fridge', {
        method: "POST",
        headers: {"X-CSRFToken": cookie.toString()},
        body: result.toString(),
    }).then(res => {
        console.log("Zapisano!");
    });
}


function showProducts(prod, frid) {
    var data = {
        Products: prod,
        Fridge: frid
    };

    const unique = [...new Set(data.Products.map(item => item.type))];

    //console.log(unique);

    //data.Products = data_products;

    var byName = data.Products.slice(0);
    byName.sort(function (a, b) {
        var x = a.name.toLowerCase();
        var y = b.name.toLowerCase();
        return x < y ? -1 : x > y ? 1 : 0;
    });

    data.Products = byName;

    var tables = {};

    var moveMe = function () {
        this.table = tables[this.table === tables.Fridge ? 'Products' : 'Fridge'];
        this.table.tbody.appendChild(this.td);
    };

    Object.keys(data).forEach(function (key) {
        var container = document.createElement('div'),
            table = tables[key] = document.createElement('table'),
            tbody = table.tbody = document.createElement('tbody');
        if (key == 'Products') {
            container.setAttribute('id', 'products');
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

            unique.forEach(function (item) {
                var opt = document.createElement("option");
                opt.setAttribute("value", item);
                var nod = document.createTextNode(item);
                opt.appendChild(nod);
                select.appendChild(opt);
            });

        } else {
            container.setAttribute('id', 'fridge')

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
    var saveButton = document.createElement("button");
    //searchButton.setAttribute('onClick','recipySearch()');
    saveButton.setAttribute('onClick', 'recipySearch()');
    saveButton.setAttribute('id', "recipySearch")
    saveButton.innerHTML = 'Save';
    search.appendChild(saveButton);
};

