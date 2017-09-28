clear

load group.txt
train_ratio=0; % train label ratio for classification task
%% hyperparameters
C=100; %hyperparameter for svm; C=5 for cora dataset C=100 for blogcatalog and flickr

%% compute row-normalized adjacency matrix A

numOfNode = 103024;
numOfGroup = 8;
group = sparse(group(:,1),group(:,2),1,numOfNode,numOfGroup);
grouptmp=group;

%% load deepwalk embeddings
load AMiner_LINE1.txt
features = AMiner_LINE1; 

% load AMiner_LINE12.txt
% features = AMiner_LINE12; 

% load AMiner_LINE2.txt
% features = AMiner_LINE2; 
%% test before NEU
% feature normalization; unnecessary for link prediction task
for i=1:size(features,2)
    if (norm(features(:,i))>0)
        features(:,i) = features(:,i)/norm(features(:,i));
    end
end


for j = 1:10
train_ratio=train_ratio+0.1;
    
micro_F1=0;
macro_F1=0;
for i=1:10  % do the procedure for 10 times and take the average
    rp = randperm(numOfNode);
    testId = rp(1:floor(numOfNode*(1-train_ratio)));

    groupTest = group(testId,:);
    group(testId,:)=[];

    trainId = [1:numOfNode]';
    trainId(testId,:)=[];

    result=SocioDim(features, group, trainId, testId, C);
    [res,b] = evaluate(result,groupTest);
    micro_F1=micro_F1+res.micro_F1;
     macro_F1=macro_F1+res.macro_F1;
    group=grouptmp;
end
train_ratio
micro_F1=micro_F1/10
macro_F1=macro_F1/10

end

% %% NEU
% features = cora_deepwalk; % initial value
% % feature normalization; unnecessary for link prediction task
% for i=1:size(features,2)
%     if (norm(features(:,i))>0)
%         features(:,i) = features(:,i)/norm(features(:,i));
%     end
% end
% 
% tic;
% for iter=1:maxIter
% features=features+lambda1*A*features+lambda2*A*(A*features);
% end
% toc;
% 
% % feature normalization; unnecessary for link prediction task
% for i=1:size(features,2)
%     if (norm(features(:,i))>0)
%         features(:,i) = features(:,i)/norm(features(:,i));
%     end
% end
% 
% %% test after NEU
% acc=0;
% for i=1:10  % do the procedure for 10 times and take the average
%     rp = randperm(numOfNode);
%     testId = rp(1:floor(numOfNode*(1-train_ratio)));
% 
%     groupTest = group(testId,:);
%     group(testId,:)=[];
% 
%     trainId = [1:numOfNode]';
%     trainId(testId,:)=[];
% 
%     result=SocioDim(features, group, trainId, testId, C);
%     [res,b] = evaluate(result,groupTest);
%     acc=acc+res.micro_F1;
%     group=grouptmp;
% end
% acc=acc/10