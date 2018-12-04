River_file_1 = fopen('Rio_01_Camargos.txt', 'r');
River_1 = fscanf(River_file_1, '%d');
for i = 1 : length(River_1)
   % disp(River_1(i));
end

River_file_2 = fopen('Rio_02_Furnas.txt', 'r');
River_2 = fscanf(River_file_2, '%d');
for i = 1 : length(River_2)
    % disp(i)
end

% sprintf('%d %d', length(River_1), length(River_2))

input_data = zeros(4, max(length(River_1), length(River_2)) - 2);
input_data(1, :) = River_1(1:end-2);
input_data(2, :) = River_1(2:end-1);
input_data(3, :) = River_2(1:end-2);
input_data(4, :) = River_2(2:end-1);

output_data = zeros(2, max(length(River_1), length(River_2)) - 2);
output_data(1, :) = River_1(3:end);
output_data(2, :) = River_2(3:end);

%% Model 1 - Levenberg-Marquardt
% trainlm: [4-20-2]

NN_1 = feedforwardnet([20]);
NN_1.trainFcn = 'trainlm';
NN_1 = configure(NN_1, input_data, output_data);
NN_1 = train(NN_1, input_data, output_data);
%% Model 2 - Levenberg_Marquardt
% trainlm: [4-20-30-25-2]

NN_2 = feedforwardnet([20, 30, 25], 'trainlm');
NN_2 = configure(NN_2, input_data, output_data);
NN_2 = train(NN_2, input_data, output_data);
%% Model 3 - Resilient Backpropagation
% trainrp: [4-190-2]

NN_3 = feedforwardnet([190], 'trainrp');
NN_3 = configure(NN_3, input_data, output_data);
NN_3 = train(NN_3, input_data, output_data);
%% Model 4 - Polak-Ribiére Conjugate
% traincgp:[4-110-2]

NN_4 = feedforwardnet([110], 'traincgp');
NN_4 = configure(NN_4, input_data, output_data);
NN_4 = train(NN_4, input_data, output_data);
%% Model 5 - Bayesian Regularization
% trainbr: [4-155-2]

NN_5 = feedforwardnet([155], 'trainbr');
NN_5 = configure(NN_5, input_data, output_data);
NN_5 = train(NN_5, input_data, output_data);

%% Model 6 - 